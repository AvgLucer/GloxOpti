# GloxOpti

<p align="center">
  <img src="banner.gif" alt="GloxOpti Demo" width="100%">
</p>

<p align="center">
  <strong>Lightweight Python Image Optimization Library</strong><br>
  Optimize PNG, JPEG and WebP images with a simple API and configurable optimization levels.
</p>

---

## Features

* 🖼️ Optimize PNG, JPEG and WebP images
* ⚡ Five configurable optimization levels
* 📦 Lightweight and easy to use
* 🐍 Built with Pillow
* 💻 Beginner-friendly API
* 🚀 Perfect for automation scripts and personal projects

---

## Installation

```bash
pip install gloxopti
```

---

## Dependencies

GloxOpti uses:

* Pillow

---

## Quick Start

```python
import gloxopti

gloxopti.ImgOpti(
    "wallpaper",
    "png",
    3
)
```

---

## Optimization Levels

| Level | Compression |
| ----: | ----------- |
|     1 | Low         |
|     2 | Moderate    |
|     3 | Balanced    |
|     4 | High        |
|     5 | Maximum     |

---

## Supported Formats

* PNG
* JPEG
* WebP

---

## Example Output

Input:

```text
wallpaper.png
```

Output:

```text
opt_wallpaper.png
```

---

## Project Structure

```text
GloxOpti/
│
├── gloxopti/
│   ├── __init__.py
│   └── GloxOpti.py
│
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

---

## Roadmap

* Image resizing
* Image format conversion
* Batch optimization
* Metadata removal
* Folder optimization
* CLI support

---

## License

Licensed under the MIT License.

---

## Author

**AvgLucer**

If you find this project useful, consider giving the repository a ⭐.
