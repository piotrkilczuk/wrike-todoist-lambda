.PHONY: default deploy

default:
	echo "Please specify a target"
	exit 1

deploy:
	sls deploy

run_local:
	sls invoke local -f sync_wrike_to_todoist

run_remote:
	sls invoke -l -f sync_wrike_to_todoist
