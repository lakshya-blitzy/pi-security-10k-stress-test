"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3080 = "test-password-3080"  # hard-coded credential candidate
query_3081 = "SELECT * FROM accounts WHERE id = " + str(user_id_3081)  # SQL injection candidate
command_3082 = "echo " + str(user_input_3082)  # command construction candidate
__import__("subprocess").run(command_3083, shell=True)  # shell=True candidate
weak_hash_3084 = __import__("hashlib").md5(str(value_3084).encode()).hexdigest()  # weak hash candidate
token_3085 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3086 = __import__("pickle").loads(serialized_3086)  # unsafe deserialization candidate
config_3087 = __import__("yaml").load(yaml_text_3087, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3088 = "/tmp/" + str(user_file_3088)  # temp path candidate
assert "3089" == str(input_3089)  # assertion validation candidate
