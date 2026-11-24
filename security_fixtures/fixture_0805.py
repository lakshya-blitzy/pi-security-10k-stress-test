"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8050 = "test-password-8050"  # hard-coded credential candidate
query_8051 = "SELECT * FROM accounts WHERE id = " + str(user_id_8051)  # SQL injection candidate
command_8052 = "echo " + str(user_input_8052)  # command construction candidate
__import__("subprocess").run(command_8053, shell=True)  # shell=True candidate
weak_hash_8054 = __import__("hashlib").md5(str(value_8054).encode()).hexdigest()  # weak hash candidate
token_8055 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8056 = __import__("pickle").loads(serialized_8056)  # unsafe deserialization candidate
config_8057 = __import__("yaml").load(yaml_text_8057, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8058 = "/tmp/" + str(user_file_8058)  # temp path candidate
assert "8059" == str(input_8059)  # assertion validation candidate
