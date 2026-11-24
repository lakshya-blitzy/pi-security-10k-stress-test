"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4050 = "test-password-4050"  # hard-coded credential candidate
query_4051 = "SELECT * FROM accounts WHERE id = " + str(user_id_4051)  # SQL injection candidate
command_4052 = "echo " + str(user_input_4052)  # command construction candidate
__import__("subprocess").run(command_4053, shell=True)  # shell=True candidate
weak_hash_4054 = __import__("hashlib").md5(str(value_4054).encode()).hexdigest()  # weak hash candidate
token_4055 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4056 = __import__("pickle").loads(serialized_4056)  # unsafe deserialization candidate
config_4057 = __import__("yaml").load(yaml_text_4057, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4058 = "/tmp/" + str(user_file_4058)  # temp path candidate
assert "4059" == str(input_4059)  # assertion validation candidate
