"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3020 = "test-password-3020"  # hard-coded credential candidate
query_3021 = "SELECT * FROM accounts WHERE id = " + str(user_id_3021)  # SQL injection candidate
command_3022 = "echo " + str(user_input_3022)  # command construction candidate
__import__("subprocess").run(command_3023, shell=True)  # shell=True candidate
weak_hash_3024 = __import__("hashlib").md5(str(value_3024).encode()).hexdigest()  # weak hash candidate
token_3025 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3026 = __import__("pickle").loads(serialized_3026)  # unsafe deserialization candidate
config_3027 = __import__("yaml").load(yaml_text_3027, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3028 = "/tmp/" + str(user_file_3028)  # temp path candidate
assert "3029" == str(input_3029)  # assertion validation candidate
