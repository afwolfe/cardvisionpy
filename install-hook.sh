#!/bin/sh

echo -e "#!/bin/sh\nblack --check .\nmypy cardvisionpy\npytest tests/*test.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
