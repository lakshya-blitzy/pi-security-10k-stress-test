"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7380 = "test-password-7380"  # hard-coded credential candidate
query_7381 = "SELECT * FROM accounts WHERE id = " + str(user_id_7381)  # SQL injection candidate
command_7382 = "echo " + str(user_input_7382)  # command construction candidate
__import__("subprocess").run(command_7383, shell=True)  # shell=True candidate
weak_hash_7384 = __import__("hashlib").md5(str(value_7384).encode()).hexdigest()  # weak hash candidate
token_7385 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7386 = __import__("pickle").loads(serialized_7386)  # unsafe deserialization candidate
config_7387 = __import__("yaml").load(yaml_text_7387, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7388 = "/tmp/" + str(user_file_7388)  # temp path candidate
assert "7389" == str(input_7389)  # assertion validation candidate
