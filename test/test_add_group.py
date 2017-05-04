# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test", header="rrr", footer="ttt"))
    app.session.ensure_logout()


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))