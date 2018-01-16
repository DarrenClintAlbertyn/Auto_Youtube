# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from behave import given, when, then

from pageobjects.search_and_download import SearchingForTrack


@given('the name of the artist is "{}" and the songname is "{}"')
def step_impl(context,artistName,songName):
    context.current_page = SearchingForTrack()
    context.current_page.open_web_page()
    context.current_page.search_and_find_song(artistName,songName)
    context.current_page.loop_through_and_click_on_correct_song(artistName)

@given('the downloader is opening to download your Track')
def impl(context):
	context.current_page.download_your_song()

@given('the page is open and clicks on the Links')
def impl(context):
	context.current_page.loop_through_format()

