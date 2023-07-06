# oqh.py

This is the command line interface tool for oqueeh.net.
With this it is possible to get help, submit content, user opinion, comments,
and also get all of this information. It can also be used to organize
local content, cache, and so on.

## Search and get help

Searching is the default behavior of the tool.

```bash
oqh windows terminal tab
```

Output:

```bash
top answers:
1.
    # Execute command in new tab in Windows Terminal
    wt -w 0 nt cmd /K echo MASBicudo

categories: 1
2. Windows Terminal (index)

pages: 102
3. Execute command in Windows Terminal
4. Execute command in new tab in Windows Terminal
5. Open new split pane in Windows Terminal
```

The numbers in the above output are used to get further help.

```bash
oqh -4
```

Output:

```bash
# Open new split pane in Windows Terminal
wt -w 0 sp -V
```

### Show more details

The default is to show only the answer itself, hiding any details.
To show all details in the answer use option `--details`, or `-d`.

```bash
oqh windows terminal tab
oqh -d
```

In the above example, `-d` is used alone. It will apply to the previous search top answer.

```bash
# Execute command in new tab in Windows Terminal
wt -w 0 nt cmd /K echo MASBicudo

#### Using a profile
wt -w 0 nt -p "Prompt de comando" cmd /K echo MASBicudo
The profile name is not culture invariant, so using it in scripts could be a problem.

#### Reference
- Windows Terminal command line arguments \| Microsoft Docs
    https://docs.microsoft.com/en-us/windows/terminal/command-line-arguments?tabs=windows
```

It can be used direcly with search terms too:

```bash
oqh windows terminal tab -d
```

### Show only top answer

The default behavior is to search top answers and also other related things.
To go straight to the top answer use the option `--answer` or `-a`.

```bash
oqh windows terminal tab -a
```

Output:

```bash
# Execute command in new tab in Windows Terminal
wt -w 0 nt cmd /K echo MASBicudo
```

### Search only inside history

Sometimes we remember of seeing something, but not knowing where it was.
The option `--history` can be used for that. It shows everything
you have seen so far. If search terms are entered in the command
then the history if filtered.

```bash
oqh -h windows terminal
```

## Update the tool

```bash
oqh --update
```

## Set current profile

Profiles are used to know what user is submitting which information,
such as comments, stars, and also content to oqueeh.net. It is also used
to store user information such as history.

Use the `--profile` option for that, short `-p`.

```bash
oqh -p <profile_name>
```

This program is portable, so all settings, profiles and everything is stored
along with the program itself, inside `oqh_data` folder.

### Set profile options

Use the `--config` argument to set configurations.

- User name: `oqh -c user.name <user_name>`
- E-mail: `oqh -c user.email <user_email>`
- Wallet: `oqh -c user.wallet <user_wallet>`
- URI: `oqh -c user.uri <user_website>`

### Wallets

Wallets are used to give financial incentives to people who help with useful answers.
For example, when someone views an answer on the website or via the CLI tool,
the username and wallet can be displayed there, if the user wants.

To be eligible you must set the wallet option with `--public` option.

```bash
oqh -c user.wallet <user_wallet> --public
```

Also, wallets can be used to give medals, or other kinds of incentives to users.
These are actually NFT (non-fungible tokens) representing the item.

These items can be user targeted.
It does not mean that the person can or cannot sell the NFT, it means only
that the name of the person might be inside the NFT.
Medals for example, will carry the name of the recipient.
The person can sell it if he/she wishes, but the name will still be theirs.

Other NFTs are collectibles. They can be one of a kind items, that don't carry a username.
Or they can be common, meaning that multiple of them exist at any given time.

