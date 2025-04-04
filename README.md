# React Native Builder
This is a simple python Scr1pt that automate the rename release apk from react native builded packege.
You can use it to simplify gradlew release and rename packege accordium your preference.

## How to install
Following the next steps:
```sh
wget https://raw.githubusercontent.com/mr0xff/react-native-android-build/refs/heads/main/build_release_name.py
cp build_release_name.py <path/to/your/project/name>/android/
```
The next step is to update your `package.json` file as following:
```json
{
  "scripts": {
    "build": "cd android/ && ./gradlew build  && ./build_release_name.py"
  }
}
```
That's all see you soon :)
