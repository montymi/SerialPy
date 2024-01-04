<div id="readme-top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1 align="center">SerialPy v0.1.0</h1>

  <p align="center">
    Precision Data Format Manager
    ·
    <a href="https://github.com/montymi/SerialPy/issues">Report Bug</a>
    ·
    <a href="https://github.com/montymi/SerialPy/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#tasks">Tasks</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

*SerialPy* is a Python package designed to streamline search and replace operations on data formats: <a style="text-decoration:none" href='https://yaml.org'>yaml</a>, <a style="text-decoration:none" href="https://toml.io/en/">toml</a>, and <a style="text-decoration:none" href="https://www.json.org/json-en.html">json</a>. 
Built to use with additional shell scripting to semi-automate workflows involving OpenAPI and Swagger files, making it ideal for companies aiming to maintain consistency within their specification sheets. 
Features include `search` and `replace`, allowing for precise control of serial data. *SerialPy* empowers users to ensure accuracy and reliability, making it an invaluable tool for specification sheet maintenance.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Installation
Simply run:
```
pip install SerialPy
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
Serialpy supports the `-h` flag at the main and all subcommands so more details can be found there.

### Command-Line Interface (CLI)
Search for any key within the data in the given file path that is "test" and return a list of values associated with the key.
```
serialpy search path/to/file "test" --find="key" --ret="value"
```
Replace any instance of "var1" from the data in the given file path to "var2" and return True if successfully written back to the file.
```
serialpy replace path/to/file "var1" "var2"
```

### Library
Import the module at the top of your python script.

The following snippet of code runs `search` on all *values* in `"path/to/file"` for 5 and returns all *keys* associated with the value, 5. 

The next line checks to see if the `replace` function successfully converted all instances of 5 in `"path/to/file"` with 6 and wrote the changes back into the file.
```
from serialpy import search, replace

found = search.values("path/to/file", "5", "keys") # add False as last argument to disable console printing
if (replace.all("path/to/file", "5", "6"):
  # code to run after successfully replacing 5 with 6
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- TASKS -->
## Tasks

- [X] Add `replace` feature
- [X] Add support for `.toml` 
- [X] Update README.md
- [ ] `search` and `replace` contained within a `Cereal` object that stores serial data
- [ ] Add support for multiple documents at once
- [ ] Add project parser to automatically insert supported file types

See the [open issues](https://github.com/montymi/SerialPy/issues) for a full list of issues and proposed features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

1. [Fork the Project](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
2. Create your Feature/Update Branch (`git checkout -b feature/NewFeature` or `git checkout -b update/Feature`)
3. Commit your Changes (`git commit -m 'Add some Feature'`)
4. Push to the Branch (`git push origin feature/NewFeature` or `git push origin update/Feature`)
5. [Open a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See [`LICENSE.txt`](https://github.com/montymi/SerialPy/blob/main/LICENSE.txt) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Michael Montanaro - [LinkedIn](https://www.linkedin.com/in/michael-montanaro/) - mcmontanaro01@gmail.com

Project Link: [https://github.com/montymi/SerialPy](https://github.com/montymi/SerialPy)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [OpenAPI/Swagger Testing](https://apitools.dev/swagger-cli/)
* [Publishing to PyPi Tutorial](https://realpython.com/pypi-publish-python-package/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/montymi/SerialPy.svg?style=for-the-badge
[contributors-url]: https://github.com/montymi/SerialPy/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/montymi/SerialPy.svg?style=for-the-badge
[forks-url]: https://github.com/montymi/SerialPy/network/members
[stars-shield]: https://img.shields.io/github/stars/montymi/SerialPy.svg?style=for-the-badge
[stars-url]: https://github.com/montymi/SerialPy/stargazers
[issues-shield]: https://img.shields.io/github/issues/montymi/SerialPy.svg?style=for-the-badge
[issues-url]: https://github.com/montymi/SerialPy/issues
[license-shield]: https://img.shields.io/github/license/montymi/SerialPy.svg?style=for-the-badge
[license-url]: https://github.com/montymi/SerialPy/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/michael-montanaro
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
