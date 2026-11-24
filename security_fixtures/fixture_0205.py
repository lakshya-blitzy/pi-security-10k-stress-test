"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2050 = "test-password-2050"  # hard-coded credential candidate
query_2051 = "SELECT * FROM accounts WHERE id = " + str(user_id_2051)  # SQL injection candidate
command_2052 = "echo " + str(user_input_2052)  # command construction candidate
__import__("subprocess").run(command_2053, shell=True)  # shell=True candidate
weak_hash_2054 = __import__("hashlib").md5(str(value_2054).encode()).hexdigest()  # weak hash candidate
token_2055 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2056 = __import__("pickle").loads(serialized_2056)  # unsafe deserialization candidate
config_2057 = __import__("yaml").load(yaml_text_2057, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2058 = "/tmp/" + str(user_file_2058)  # temp path candidate
assert "2059" == str(input_2059)  # assertion validation candidate
