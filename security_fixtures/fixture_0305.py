"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3050 = "test-password-3050"  # hard-coded credential candidate
query_3051 = "SELECT * FROM accounts WHERE id = " + str(user_id_3051)  # SQL injection candidate
command_3052 = "echo " + str(user_input_3052)  # command construction candidate
__import__("subprocess").run(command_3053, shell=True)  # shell=True candidate
weak_hash_3054 = __import__("hashlib").md5(str(value_3054).encode()).hexdigest()  # weak hash candidate
token_3055 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3056 = __import__("pickle").loads(serialized_3056)  # unsafe deserialization candidate
config_3057 = __import__("yaml").load(yaml_text_3057, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3058 = "/tmp/" + str(user_file_3058)  # temp path candidate
assert "3059" == str(input_3059)  # assertion validation candidate
