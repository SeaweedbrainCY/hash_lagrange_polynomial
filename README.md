# Cryptographic hash function based on the Lagrange Polynomial
This repository hosts the code of a whole new cryptographic function, using the Lagrange Polynomial. A new hashing polynomial has been created by myself. The justification, and the explicit method is explained (in french) in the following paper : [Study paper](https://devnathan.github.io/source/TIPE.pdf)

#### ⚠️ WARNING : This is NOT a secured cryptographic function. 
No security proof has been made. It has been created in order to give an pratical and efficient example of what can be done with that method. This should not be used for other reason than study and absolutely not for security reasons.


#### Contributor(s) : [@DevNathan](https://github.com/DevNathan) (Nathan Stchepinsky)
![GitHub Contributors Image](https://contrib.rocks/image?repo=devnathan/RhoPollard)

## Licence

[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

This code source is published under GPLv3 licence.

    Copyright (C) 2021  Nathan Stchepinsky

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Usage
### 1 - Clone the project
Clone this project on your laptop by using this [link](https://github.com/DevNathan/hash_lagrange_polynomial/archive/refs/heads/main.zip) or by executing the following command in your terminal :
```
git clone https://github.com/DevNathan/hash_lagrange_polynomial
```
### 2 - Hashing a message

```python
from hash_lagrange import *

hash_len = 32 # Length of the produced hash (in char)

lagrange = Lagrange(hash_len)

message = "Hello world!"

hash = lagrange.hash(message)
```

### 3 - Output 
Hashing "Hello world !" on 32 char.
```
🔒 Hash :  kk31q6ojgqeeihwfshzus1f1xxek84xa


** Sucessfuly hashed in  0.013  seconds **
```
You can see more example, including proof of the padding and the avalanche effect, in the [study paper]((https://devnathan.github.io/source/TIPE.pdf)
)
