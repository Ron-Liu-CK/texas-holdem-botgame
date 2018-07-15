#!/usr/bin/env bash

echo $0
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

function build_client() {
    clientPath=$1
    zipFileName=$2
    downloadFolder=$3

    targetFile="${zipFileName}.zip"

    echo ${targetFile}

    cd /tmp
    rm -rf ${zipFileName}
    cp -r ${clientPath} ${zipFileName}
    zip -r ${targetFile} ${zipFileName} 
    cd ${downloadFolder}
    rm -f ${targetFile}
    cp /tmp/${targetFile} ${targetFile}
}

echo "[-] Building Java bot client ....."
build_client "${SCRIPTPATH}/java-client" "holdem-bot-java-client" "${SCRIPTPATH}/../server/src/main/webapp/resources/clients"
echo "[-] Building NodeJS bot client ....."
build_client "${SCRIPTPATH}/nodejs-client" "holdem-bot-nodejs-client" "${SCRIPTPATH}/../server/src/main/webapp/resources/clients"
echo "[-] Building Python bot client ....."
build_client "${SCRIPTPATH}/python-client" "holdem-bot-python-client" "${SCRIPTPATH}/../server/src/main/webapp/resources/clients"

echo "[+] Done !!!!!"
