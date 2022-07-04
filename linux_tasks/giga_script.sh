#!/bin/bash

function menu(){
    echo "" ; echo "Hello! We have some of Ivaylo's tasks here." ; echo ""
    echo "Which task do you want to see?"
    echo "1. Regex"
    echo "2. Processes"
    echo "3. Access.log"
    echo "4. Bash script"
    echo "0. Exit"

    echo "" ; read TASK ; echo ""

    case $TASK in

        1)
            task_one ; echo "" ; echo "Back to menu? (y/n)" ; read ANSWER ;
            [[ $ANSWER == "y" ]] && menu || echo "Goodbye!" ; exit 1 ;;
        2)
            task_two ; echo "" ; echo "Back to menu? (y/n)" ; read ANSWER ;
            [[ $ANSWER == "y" ]] && menu || echo "Goodbye!" ; exit 1 ;;
        3)
            task_three ; echo "" ; echo "Back to menu? (y/n)" ; read ANSWER ;
            [[ $ANSWER == "y" ]] && menu || echo "Goodbye!" ; exit 1 ;;
        4)
            task_four ; echo "" ; echo "Back to menu? (y/n)" ; read ANSWER ;
            [[ $ANSWER == "y" ]] && menu || echo "Goodbye!" ; exit 1 ;;
        0)
            echo "Goodbye!" ; exit 1 ;;
        *)
            echo "Unknown command" ; echo "" ; echo "Try again? (y/n)" ; read ANSWER ;
            [[ $ANSWER == "y" ]] && menu || echo "Goodbye!" ; exit 1 ;;
    esac
}

function task_one(){
    echo "Current time" ; echo ""
    echo '''date | grep -oE "([0-9]+:[0-9]+:[0-9]+)"''' ; echo "" ; echo ""
    sleep 1
    echo "IPv4 Address" ; echo ""
    echo '''ifconfig | grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"''' ; echo "" ; echo ""
    sleep 1
    echo "Whole paragraph" ; echo ""
    echo '''grep -oE "^(.+?)\n"''' ; echo "" ; echo ""
}

function task_two(){
    echo '''ps -eF | awk "{print $1; $2}" | grep $USER | awk "{print $2}"'''
}

function task_three(){
    echo '''cat access.log | awk "{print $1}" | sort -n | uniq -c | sort -nr'''
}

function task_four(){
    echo "Check:"
    echo "1. Number of CPU cores"
    echo "2. Disk space"
    echo "3. Size of RAM"
    echo "4. Last users to login"
    echo "5. Number of active Python/Perl processes"
    echo "0. Go back"

    echo "" ; read CHOICE ; echo ""

    case $CHOICE in

        1)
            SOLUTION=$(nproc)
            echo "You have $SOLUTION CPU cores." ; echo ""
            echo "Check another thing? (y/n)"
            read ANSWER
            [[ $ANSWER == "y" ]] && task_four || echo "Goodbye!" ; menu ;;
        2)
            SOLUTION=$(df | awk '{sum += $2} END {printf("%.2f\n", sum / 1000000)}')
            echo "You have a total of $SOLUTION GB of disk space." ; echo ""
            echo "Check another thing? (y/n)"
            read ANSWER
            [[ $ANSWER == "y" ]] && task_four || echo "Goodbye!" ; menu ;;
        3)
            SOLUTION=$(grep MemTotal /proc/meminfo | awk '{printf("%.2f\n", $2 / 1000000)}')
            echo "You have $SOLUTION GB RAM." ; echo ""
            echo "Check another thing? (y/n)"
            read ANSWER
            [[ $ANSWER == "y" ]] && task_four || echo "Goodbye!" ; menu ;;
        4)
            SOLUTION=$(last -10 | grep -v 'reboot' | awk 'NR<6 {print $1}')
            echo "The last users to login:" ; echo "" ; echo $SOLUTION ; echo ""
            echo "Check another thing? (y/n)"
            read ANSWER
            [[ $ANSWER == "y" ]] && task_four || echo "Goodbye!" ; menu ;;
        5)
            SOLUTION=$(ps -ef | grep -E 'python|perl' | wc -l)
            echo "You have $SOLUTION Python/Perl processes running right now." ; echo ""
            echo "Check another thing? (y/n)"
            read ANSWER
            [[ $ANSWER == "y" ]] && task_four || echo "Goodbye!" ; menu ;;
        0)
            menu ;;
        *)
            echo "Unknown command"
            echo "Try again? (y/n)"
            [[ $ANSWER == "y" ]] && task_four || menu ;;
    esac
}

menu
