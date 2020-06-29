Changelog
=========


(unreleased)
------------

Fix
~~~
- Harmonize the sunrise preset with the others. [Stavros Korokithakis]
- Fix exception when used with white bulbs (#3) [pklapperich]

  * White bulbs don't have rgb, hue, or saturation. Print "None" for NoneType.

  * Add comment
- Add stderr output to hex_to_color (#4) [pklapperich]

  * Add stderr output to hex_to_color
  rather than just setting red without telling the user WTF happened

  * Fix error message
- Add default value for sunrise preset; fixes exception (#5)
  [pklapperich]

  * Add default value for sunrise preset; fixes exception

  * Remove default from function
- Print the rgb color in hex in the `status` command (#1) [Семён
  Марьясин]
- Add arguments to two presets. [Stavros Korokithakis]
- Make the pulse command leave the bulb the way it found it. [Stavros
  Korokithakis]
- Use the latest yeelight library. [Stavros Korokithakis]

Other
~~~~~
- Add pre-commit. [Stavros Korokithakis]
- Add mention of development mode in the README. [Stavros Korokithakis]
- Style code. [Stavros Korokithakis]
- Add sunrise preset (#2) [Семён Марьясин]
- Test: Don't run the (nonfunctional) tests. [Stavros Korokithakis]
- Test: Appease the linter. [Stavros Korokithakis]
- Test: Use Python 3.5 as default. [Stavros Korokithakis]
- Chore: Pin requirements. [Stavros Korokithakis]
- 0.1.0. [semantic-release]
- Feat: Add more presets. [Stavros Korokithakis]
- Refactor: Update the yeelight library and move to its transitions.
  [Stavros Korokithakis]
- Doc: Update README. [Stavros Korokithakis]
- Fix style more. [Stavros Korokithakis]
- Fix style. [Stavros Korokithakis]
- Update .gitlab_ci.yml. [Stavros Korokithakis]
- 0.0.16. [semantic-release]
- Feat: Add preset stop command. [Stavros Korokithakis]
- Feat: Add BPM option to the disco preset. [Stavros Korokithakis]
- Doc: Add more commands in the README. [Stavros Korokithakis]
- Doc: Format README better. [Stavros Korokithakis]
- Doc: Add features. [Stavros Korokithakis]
- 0.0.15. [semantic-release]
- Feat: Add short options. [Stavros Korokithakis]
- 0.0.14. [semantic-release]
- Feat: Add presets. [Stavros Korokithakis]
- 0.0.13. [semantic-release]
- Feat: Add disco mode. [Stavros Korokithakis]
- Feat: Add preliminary multiple bulb support. [Stavros Korokithakis]
- 0.0.12. [semantic-release]
- 0.0.11. [semantic-release]
- Add pulse command. [Stavros Korokithakis]
- 0.0.10. [semantic-release]
- Feat: Support multiple bulbs. [Stavros Korokithakis]
- 0.0.9. [semantic-release]
- Make library Python 2 compatible. [Stavros Korokithakis]
- Fix setup. [Stavros Korokithakis]
- 0.0.8. [semantic-release]
- Specify the correct version for yeelight. [Stavros Korokithakis]
- Migrate to the yeelight library. [Stavros Korokithakis]
- 0.0.7. [semantic-release]
- 0.0.6. [semantic-release]
- 0.0.5. [semantic-release]
- Fix requirements. [Stavros Korokithakis]
- Fix import error importing version. [Stavros Korokithakis]
- 0.0.4. [semantic-release]
- 0.0.3. [semantic-release]
- Remove Python 3.6 from tests. [Stavros Korokithakis]
- 0.0.2. [semantic-release]
- First version. [Stavros Korokithakis]
- Add README. [Stavros Korokithakis]


