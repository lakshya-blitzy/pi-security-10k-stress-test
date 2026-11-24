"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3380 = "test-password-3380"  # hard-coded credential candidate
query_3381 = "SELECT * FROM accounts WHERE id = " + str(user_id_3381)  # SQL injection candidate
command_3382 = "echo " + str(user_input_3382)  # command construction candidate
__import__("subprocess").run(command_3383, shell=True)  # shell=True candidate
weak_hash_3384 = __import__("hashlib").md5(str(value_3384).encode()).hexdigest()  # weak hash candidate
token_3385 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3386 = __import__("pickle").loads(serialized_3386)  # unsafe deserialization candidate
config_3387 = __import__("yaml").load(yaml_text_3387, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3388 = "/tmp/" + str(user_file_3388)  # temp path candidate
assert "3389" == str(input_3389)  # assertion validation candidate
