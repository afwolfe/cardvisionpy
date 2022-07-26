#!/bin/sh

echo -e "#!/bin/sh\nmypy cardvisionpy\npytest tests/*" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
