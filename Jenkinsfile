pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        disableConcurrentBuilds()
    }

    environment {
        STUDENT_NAME = 'Kanagat'
        STUDENT_SURNAME = 'Beken'
        STUDENT_GROUP = 'IT2-2307'
        STUDENT_ID = '38052'

        IMAGE_NAME = 'beken-kanagat-devops'
        CONTAINER_NAME = 'beken-kanagat-jenkins-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log -1 --oneline'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile app/main.py'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 - <<'PY'
import os
from app.main import student_info

output = student_info()

for value in (
    os.environ["STUDENT_NAME"],
    os.environ["STUDENT_SURNAME"],
    os.environ["STUDENT_GROUP"],
    os.environ["STUDENT_ID"],
):
    assert value in output, f"Expected value not found: {value}"

assert "Application is running successfully!" in output
print(output)
print("Application test passed")
PY
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t "$IMAGE_NAME:$BUILD_NUMBER" .'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    if docker container inspect "$CONTAINER_NAME" >/dev/null 2>&1; then
                        docker rm -f "$CONTAINER_NAME"
                    fi

                    docker run -d \
                      --name "$CONTAINER_NAME" \
                      -p 8001:8000 \
                      -e STUDENT_NAME="$STUDENT_NAME" \
                      -e STUDENT_SURNAME="$STUDENT_SURNAME" \
                      -e STUDENT_GROUP="$STUDENT_GROUP" \
                      -e STUDENT_ID="$STUDENT_ID" \
                      "$IMAGE_NAME:$BUILD_NUMBER"

                    python3 - <<'PY'
import time
from urllib.request import urlopen

url = "http://127.0.0.1:8001"

for attempt in range(20):
    try:
        with urlopen(url, timeout=2) as response:
            result = response.read().decode("utf-8")
        break
    except Exception:
        time.sleep(1)
else:
    raise RuntimeError("Application did not respond on port 8001")

print(result)

for expected in ("Kanagat", "Beken", "IT2-2307", "38052"):
    assert expected in result, f"Expected value not found: {expected}"

print("Docker container HTTP check passed")
PY

                    docker logs "$CONTAINER_NAME"
                    docker ps --filter "name=$CONTAINER_NAME"
                '''
            }
        }
    }

    post {
        success {
            echo 'DevOps Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
