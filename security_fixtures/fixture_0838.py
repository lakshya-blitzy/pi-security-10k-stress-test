"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8380 = "test-password-8380"  # hard-coded credential candidate
query_8381 = "SELECT * FROM accounts WHERE id = " + str(user_id_8381)  # SQL injection candidate
command_8382 = "echo " + str(user_input_8382)  # command construction candidate
__import__("subprocess").run(command_8383, shell=True)  # shell=True candidate
weak_hash_8384 = __import__("hashlib").md5(str(value_8384).encode()).hexdigest()  # weak hash candidate
token_8385 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8386 = __import__("pickle").loads(serialized_8386)  # unsafe deserialization candidate
config_8387 = __import__("yaml").load(yaml_text_8387, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8388 = "/tmp/" + str(user_file_8388)  # temp path candidate
assert "8389" == str(input_8389)  # assertion validation candidate
