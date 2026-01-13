a() {
printf "\033[3;93m Adding shortcut command\033[1;0m lg"
cd $PREFIX/bin
cat >> lg << EOF
xdg-open https://github.com/logout
EOF
chmod 777 lg

}
command -v lg || a
