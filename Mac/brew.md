# Homebrew

## Install
```sh
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
- See version
```sh
brew -v
```

## Update
- Update self:
```sh
brew update
```
- See outdated packages
```sh
brew outdated
```
- Upgrade all outdated packages
```sh
brew upgrade
```

## Pause and Resume Installation
- Pause
```sh
brew pin $FORMULA
```
- Resume
```sh
brew unpin $FORMULA
```

## Remove Packages
- Clean up a specific package
```sh
brew cleanup $FORMULA
```
- Clean up all
```sh
brew cleanup
```
- Check clean up packages
```sh
brew cleanup -n
```
- Just remove, no upgrade
```sh
brew uninstall formula_name --force
```