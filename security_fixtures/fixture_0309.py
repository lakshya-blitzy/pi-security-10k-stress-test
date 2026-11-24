"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3090 = "test-password-3090"  # hard-coded credential candidate
query_3091 = "SELECT * FROM accounts WHERE id = " + str(user_id_3091)  # SQL injection candidate
command_3092 = "echo " + str(user_input_3092)  # command construction candidate
__import__("subprocess").run(command_3093, shell=True)  # shell=True candidate
weak_hash_3094 = __import__("hashlib").md5(str(value_3094).encode()).hexdigest()  # weak hash candidate
token_3095 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3096 = __import__("pickle").loads(serialized_3096)  # unsafe deserialization candidate
config_3097 = __import__("yaml").load(yaml_text_3097, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3098 = "/tmp/" + str(user_file_3098)  # temp path candidate
assert "3099" == str(input_3099)  # assertion validation candidate
