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

ad_set_id = fixtures.create_adset().get_id()

# _DOC oncall [pruno]
# _DOC open [ADSET_GET_ADGROUPS_ADS_MANAGEMENT_UI]
# _DOC vars [ad_set_id]
from facebookads.objects import AdSet, Ad

fields = [
    Ad.Field.name,
    Ad.Field.configured_status,
    Ad.Field.effective_status,
    Ad.Field.creative,
]

params = {
    Ad.Field.effective_status: [
        'ACTIVE',
        'PAUSED',
        'PENDING_REVIEW',
        'PREAPPROVED',
    ],
}

ad_set = AdSet(ad_set_id)
ads = ad_set.get_ads(fields=fields, params=params)
# _DOC close [ADSET_GET_ADGROUPS_ADS_MANAGEMENT_UI]
