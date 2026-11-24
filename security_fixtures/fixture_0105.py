"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1050 = "test-password-1050"  # hard-coded credential candidate
query_1051 = "SELECT * FROM accounts WHERE id = " + str(user_id_1051)  # SQL injection candidate
command_1052 = "echo " + str(user_input_1052)  # command construction candidate
__import__("subprocess").run(command_1053, shell=True)  # shell=True candidate
weak_hash_1054 = __import__("hashlib").md5(str(value_1054).encode()).hexdigest()  # weak hash candidate
token_1055 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1056 = __import__("pickle").loads(serialized_1056)  # unsafe deserialization candidate
config_1057 = __import__("yaml").load(yaml_text_1057, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1058 = "/tmp/" + str(user_file_1058)  # temp path candidate
assert "1059" == str(input_1059)  # assertion validation candidate
