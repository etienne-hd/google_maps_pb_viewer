# google_maps_pb_viewer
[![Latest version](https://img.shields.io/pypi/v/google_maps_pb_viewer?style=for-the-badge)](https://pypi.org/project/google_maps_pb_viewer)
[![GitHub license](https://img.shields.io/github/license/etienne-hd/google_maps_pb_viewer?style=for-the-badge)](https://github.com/etienne-hd/google_maps_pb_viewer/blob/master/LICENSE)

*Visualize and pretty-print encoded Google Maps `pb` parameters.*

`google_maps_pb_viewer` is a CLI tool that decodes Google Maps encoded protobuf-like `pb` strings (starting with `!`) and prints their structure in a readable format.

## Usage

```bash
decode_pb '!3m1!4b1!4m6!3m5!1s0x47e66e2964e34e2d:0x8ddca9ee380ef7e0!8m2!3d48.8583701!4d2.2944813!16zL20vMDJqODE'
3: {
    4: true
}
4: {
    3: {
        1: 0x47e66e2964e34e2d:0x8ddca9ee380ef7e0
        8: {
            3: 48.8583701
            4: 2.2944813
        }
        16: L20vMDJqODE
    }
}
```

## Help
```
usage: decode_pb [-h] [-i INDENT] pb

Decode and pretty-print a Google Maps encoded protobuf string.

positional arguments:
  pb                    Encoded Google Maps protobuf string (starting with '!').

options:
  -h, --help            show this help message and exit
  -i INDENT, --indent INDENT
                        Number of spaces used for output indentation (default: 4).
```

## Install
```bash
pip install google_maps_pb_viewer
```

## License
This project is licensed under the MIT License.

## Support

<a href="https://www.buymeacoffee.com/etienneh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

You can reach out to me on [Telegram](https://t.me/etienne_hd) or [Discord](https://discord.com/users/1153975318990827552) if you're looking for custom scraping services.