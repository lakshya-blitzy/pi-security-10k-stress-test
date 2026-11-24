"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3200 = "test-password-3200"  # hard-coded credential candidate
query_3201 = "SELECT * FROM accounts WHERE id = " + str(user_id_3201)  # SQL injection candidate
command_3202 = "echo " + str(user_input_3202)  # command construction candidate
__import__("subprocess").run(command_3203, shell=True)  # shell=True candidate
weak_hash_3204 = __import__("hashlib").md5(str(value_3204).encode()).hexdigest()  # weak hash candidate
token_3205 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3206 = __import__("pickle").loads(serialized_3206)  # unsafe deserialization candidate
config_3207 = __import__("yaml").load(yaml_text_3207, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3208 = "/tmp/" + str(user_file_3208)  # temp path candidate
assert "3209" == str(input_3209)  # assertion validation candidate
