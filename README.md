fontcrypt
=========

Fun with web fonts.

Dependencies
------------
```
$ easy_install fontTools
```

Example
-------
```
$ python fontcrypt.py OpenSans-Regular.ttf OpenSans-Regular-Encoded.ttf

-- ENCODING KEY --
2150-2270-2357-242d-257d-276c-2862-295a-2a2b-2b60-2c63-2d66-2e44-2f40-307a-312a-3223-3349-3458-3528-3674-374a-386d-
3931-3a4b-3b59-3d5d-3f32-4065-415c-422e-4343-4434-4536-4647-474e-482c-4969-4a4d-4b3d-4c79-4d35-4e55-4f33-507c-517e-
5230-5337-5464-5521-5654-5729-584c-5948-5a42-5b53-5c38-5d3a-5e27-5f67-6022-615f-624f-636a-6478-6568-6656-6724-686e-
6961-6a39-6b2f-6c52-6d45-6e72-6f7b-7046-713b-7225-7375-745e-756f-7641-7773-786b-795b-7a71-7b77-7c3f-7d51-7e76

-- DECODING KEY --
2155-2260-2332-2467-2572-275e-2835-2957-2a31-2b2a-2c48-2d24-2e42-2f6b-3052-3139-323f-334f-3444-354d-3645-3753-385c-
396a-3a5d-3b71-3d4b-3f7c-402f-4176-425a-4343-442e-456d-4670-4746-4859-4933-4a37-4b3a-4c58-4d4a-4e47-4f62-5021-517d-
526c-535b-5456-554e-5666-5723-5834-593b-5a29-5b79-5c41-5d3d-5e74-5f61-602b-6169-6228-632c-6454-6540-662d-675f-6865-
6949-6a63-6b78-6c27-6d38-6e68-6f75-7022-717a-726e-7377-7436-7573-767e-777b-7864-794c-7a30-7b6f-7c50-7d25-7e51
```
Now `user@example.com` can be replaced with `ouh%ehk_EFRhDj{E` and still be legible with an appropriate font and supporting browser.

License
-------
```
Copyright (C) 2012 Simon Ratner

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```