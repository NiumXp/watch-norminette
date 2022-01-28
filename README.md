# watch-norminette
Um script em Python que fica observando uma pasta e rodando o norminette nos arquivos quando forem salvos

## Instalação
Clone o repositório com o seguinte comando:

```sh
git clone https://github.com/NiumXp/watch-norminette.git
```

..instale os comandos `wn` e `watch-norminette` utilizando
```sh
pip install ./watch-norminette
export PATH=/home/coder/.local/bin:$PATH
```

## Trapaça
Esse script foi desenvolvido para rodar o [norminette](https://github.com/42School/norminette) da 42 toda vez que um arquivo for salvo e mostrar no terminal, mas pode ser considerado trapaça utilizar o watch-norminette no *basecamp* já que
> "Durante avaliações, o camper precisa ter total conhecimento do código e das ferramentas que usa."

Se você não souber como o código funciona, não utilize, caso esteja confuso em alguma parte, abra uma Issue e tire sua dúvida!

## Exemplos
> Você pode utilizar `wn` e/ou `watch-norminette` para utilizar o script.

### Sem flags
Utilizando apenas `watch-norminette` o script irá observar o *path* atual e toda vez que um
arquivo for salvo ele mostrará seus erros, se tiver.

```
coder@nximenes-workspace-6cc74fc6b8-xm6kf:~$ watch-norminette
/home/coder/watch/teste.c:17:9  Found space when expecting tab
/home/coder/watch/teste.c:20:1  Empty line in function
/home/coder/watch/teste.c:21:12 Return value must be in parenthesis

[!] https://github.com/NiumXp/watch-norminette
```

### --errors
Utilizando a flag `--errors`, o script irá coletar todos os arquivos e mostrar a
quantidade dos que possuem erros.

```
coder@nximenes-workspace-6cc74fc6b8-xm6kf:~$ watch-norminette --errors
  2 /home/coder/a.c
 22 /home/coder/b.c
  4 /home/coder/watch/teste.c

[!] https://github.com/NiumXp/watch-norminette
```
