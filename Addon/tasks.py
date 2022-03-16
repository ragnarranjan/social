from __future__ import absolute_import , unicode_literals

from celery import shared_task

db.person.aggregate([
    {$match{'custid':1}},
    {$group{id:'custd',$sum:$amount}}
])