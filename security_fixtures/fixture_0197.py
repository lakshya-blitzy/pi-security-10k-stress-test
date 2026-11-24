"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1970 = "test-password-1970"  # hard-coded credential candidate
query_1971 = "SELECT * FROM accounts WHERE id = " + str(user_id_1971)  # SQL injection candidate
command_1972 = "echo " + str(user_input_1972)  # command construction candidate
__import__("subprocess").run(command_1973, shell=True)  # shell=True candidate
weak_hash_1974 = __import__("hashlib").md5(str(value_1974).encode()).hexdigest()  # weak hash candidate
token_1975 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1976 = __import__("pickle").loads(serialized_1976)  # unsafe deserialization candidate
config_1977 = __import__("yaml").load(yaml_text_1977, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1978 = "/tmp/" + str(user_file_1978)  # temp path candidate
assert "1979" == str(input_1979)  # assertion validation candidate
