# cli-ai

A commmand-line tool for unix-like pipe-based workflows, which uses a local (or remote) KoboldAI server as a shared model, so as to avoid wasting resources with multiple models and avoid huge startup times.

## Usage

For now, this just takes a single argument, the prompt, and outputs the result.

### Examples:

```
$ ai "list likely causes of the unix error code $ERRCODE" | dialog --title "Error $ERRCODE" --msgbox - 10 50
```

## Future

In future, I'll make this support more typical unix workflows, such as giving it a list of files as arguments, and piping input to it.

### FUTURE Examples:

```
$ ai < problem.txt > solution.txt "Please propose a solution for this problem: "
```

```
$ cat filelist.txt | grep wednesday | xargs ai "List these log files in order of likely anomalous behaviours that I should read first:"
```

The last example would require a model with a lot of context capacity, but hey, that's up to your model ;)

### Contributions

Any contributions that get this tool closer to the above "FUTURE examples", improve robustness, or improve security, or usability (for example, better built-in usage docs) are welcome -- just submit a PR -- but I'll get to it eventually if not.

### Authors / Contact

- Lee Braiden <leebraid@gmail.com>

