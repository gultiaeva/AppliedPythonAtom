#!/usr/bin/env python
# coding: utf-8
from collections import deque, Counter


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.events = deque()

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        self.events.appendleft({'UID': user_id, 'time': time})

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        counter = Counter()
        for event in self.events:
            if time - self.FIVE_MIN < event['time'] <= time:
                counter[event['UID']] += 1

        activity_count = list(counter.values()).count(count)
        return activity_count
