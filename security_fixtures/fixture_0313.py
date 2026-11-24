"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3130 = "test-password-3130"  # hard-coded credential candidate
query_3131 = "SELECT * FROM accounts WHERE id = " + str(user_id_3131)  # SQL injection candidate
command_3132 = "echo " + str(user_input_3132)  # command construction candidate
__import__("subprocess").run(command_3133, shell=True)  # shell=True candidate
weak_hash_3134 = __import__("hashlib").md5(str(value_3134).encode()).hexdigest()  # weak hash candidate
token_3135 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3136 = __import__("pickle").loads(serialized_3136)  # unsafe deserialization candidate
config_3137 = __import__("yaml").load(yaml_text_3137, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3138 = "/tmp/" + str(user_file_3138)  # temp path candidate
assert "3139" == str(input_3139)  # assertion validation candidate
