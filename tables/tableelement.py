# coding: utf-8
# page title: Beginner Help On Tableview In UI Module | omz:forum
# url: https://forum.omz-software.com/topic/3576/beginner-help-on-tableview-in-ui-module/7
# Aug 23, 2018 at 7:13 AM
# 
# 
# 
import ui

f = (0, 0, 600, 800)
tbl = ui.TableView(frame=f, name='Table' )
tbl.data_source = ui.ListDataSource(items=range(40))
tbl.present('sheet', title_bar_color = 'teal')