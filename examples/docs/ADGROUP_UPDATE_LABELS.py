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
from facebookads.objects import AdLabel

ad_label_id = fixtures.create_adlabel().get_id()
ad_label_name = fixtures.create_adlabel()[AdLabel.Field.name]
ad_id = fixtures.create_ad().get_id()

# _DOC oncall [ritu]
# _DOC open [ADGROUP_UPDATE_LABELS]
# _DOC vars [ad_id, ad_label_id, ad_label_name:s]
from facebookads.objects import Ad, AdLabel

ad = Ad(ad_id)
ad[Ad.Field.adlabels] = [
    {AdLabel.Field.id: ad_label_id},
    {AdLabel.Field.name: ad_label_name},
]
ad.remote_update()
# _DOC close [ADGROUP_UPDATE_LABELS]
