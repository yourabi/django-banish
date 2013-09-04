# Copyright 2008-2010 Yousef Ourabi

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import datetime

from django.db import models


class Banishment(models.Model):
    id = models.AutoField(primary_key=True)

    # Flush out time constrained banned in future revisions
    # ban_start = models.DateField(help_text="Banish Start Date.")
    # ban_stop = models.DateField(help_text="Banish Stop Date.")
    # ban_is_permanent = models.BooleanField(help_text="Is Ban Permanent? (Start/Stop ignored)")

    ban_reason = models.CharField(max_length=255, help_text="Reason for the ban?")

    BAN_TYPES = (
        ('ip-address', 'IP Address'),
        ('user-agent', 'User Agent'),
    )

    type = models.CharField(
        max_length=20,
        choices=BAN_TYPES,
        default=0,
        help_text="Type of User Ban to store"
    )

    condition = models.CharField(
        max_length=255,
        help_text='Some descriptive text goes here'
    )

    def __unicode__(self):
        return "Banished %s %s " % (self.type, self.condition)

    def __str__(self):
        return self.__unicode__()

    def is_current(self):
        """
        Determine if this banishment is current by comparing
        dates
        """
        if self.permanent or self.stop > datetime.date.today(): 
            return True
        return False

    class Meta:
        permissions = (("can_ban_user", "Can Ban User"),)
        verbose_name = "Banishments"
        verbose_name_plural = "Banishments"
        db_table = 'banishments'
