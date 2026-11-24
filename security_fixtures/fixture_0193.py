"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1930 = "test-password-1930"  # hard-coded credential candidate
query_1931 = "SELECT * FROM accounts WHERE id = " + str(user_id_1931)  # SQL injection candidate
command_1932 = "echo " + str(user_input_1932)  # command construction candidate
__import__("subprocess").run(command_1933, shell=True)  # shell=True candidate
weak_hash_1934 = __import__("hashlib").md5(str(value_1934).encode()).hexdigest()  # weak hash candidate
token_1935 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1936 = __import__("pickle").loads(serialized_1936)  # unsafe deserialization candidate
config_1937 = __import__("yaml").load(yaml_text_1937, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1938 = "/tmp/" + str(user_file_1938)  # temp path candidate
assert "1939" == str(input_1939)  # assertion validation candidate
