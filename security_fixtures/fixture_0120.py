"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1200 = "test-password-1200"  # hard-coded credential candidate
query_1201 = "SELECT * FROM accounts WHERE id = " + str(user_id_1201)  # SQL injection candidate
command_1202 = "echo " + str(user_input_1202)  # command construction candidate
__import__("subprocess").run(command_1203, shell=True)  # shell=True candidate
weak_hash_1204 = __import__("hashlib").md5(str(value_1204).encode()).hexdigest()  # weak hash candidate
token_1205 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1206 = __import__("pickle").loads(serialized_1206)  # unsafe deserialization candidate
config_1207 = __import__("yaml").load(yaml_text_1207, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1208 = "/tmp/" + str(user_file_1208)  # temp path candidate
assert "1209" == str(input_1209)  # assertion validation candidate
