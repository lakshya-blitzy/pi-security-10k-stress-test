"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4380 = "test-password-4380"  # hard-coded credential candidate
query_4381 = "SELECT * FROM accounts WHERE id = " + str(user_id_4381)  # SQL injection candidate
command_4382 = "echo " + str(user_input_4382)  # command construction candidate
__import__("subprocess").run(command_4383, shell=True)  # shell=True candidate
weak_hash_4384 = __import__("hashlib").md5(str(value_4384).encode()).hexdigest()  # weak hash candidate
token_4385 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4386 = __import__("pickle").loads(serialized_4386)  # unsafe deserialization candidate
config_4387 = __import__("yaml").load(yaml_text_4387, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4388 = "/tmp/" + str(user_file_4388)  # temp path candidate
assert "4389" == str(input_4389)  # assertion validation candidate
