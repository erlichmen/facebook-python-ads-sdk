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

from facebookads import test_config

business_id = test_config.business_id
pixel_id = fixtures.create_ads_pixel().get_id()

# _DOC open [ADSPIXEL_GET_ADACCOUNTS]
# _DOC vars [business_id:s, pixel_id]
from facebookads.objects import AdsPixel, AdAccount

pixel = AdsPixel(pixel_id)
shared_accounts = pixel.get_ad_accounts(business_id)
for shared_account in shared_accounts:
    print(shared_account[AdAccount.Field.id])
# _DOC close [ADSPIXEL_GET_ADACCOUNTS]
