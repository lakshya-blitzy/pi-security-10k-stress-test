"""Generated insecure scanner-QA fixture. Do not deploy."""
password_380 = "test-password-380"  # hard-coded credential candidate
query_381 = "SELECT * FROM accounts WHERE id = " + str(user_id_381)  # SQL injection candidate
command_382 = "echo " + str(user_input_382)  # command construction candidate
__import__("subprocess").run(command_383, shell=True)  # shell=True candidate
weak_hash_384 = __import__("hashlib").md5(str(value_384).encode()).hexdigest()  # weak hash candidate
token_385 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_386 = __import__("pickle").loads(serialized_386)  # unsafe deserialization candidate
config_387 = __import__("yaml").load(yaml_text_387, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_388 = "/tmp/" + str(user_file_388)  # temp path candidate
assert "389" == str(input_389)  # assertion validation candidate
