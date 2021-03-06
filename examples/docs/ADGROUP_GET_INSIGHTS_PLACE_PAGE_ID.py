# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from examples.docs import fixtures

ad_id = fixtures.create_ad().get_id()

# _DOC oncall [pruno]
# _DOC open [ADGROUP_GET_INSIGHTS_PLACE_PAGE_ID]
# _DOC vars [ad_id]
from facebookads.objects import Ad, Insights

fields = [
    Insights.Field.impressions,
    Insights.Field.call_to_action_clicks,
]

params = {
    'breakdowns': Insights.Breakdown.place_page_id,
}

ad = Ad(ad_id)
insights = ad.get_insights(fields, params)
# _DOC close [ADGROUP_GET_INSIGHTS_PLACE_PAGE_ID]
