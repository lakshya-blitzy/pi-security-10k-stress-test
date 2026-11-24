"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5380 = "test-password-5380"  # hard-coded credential candidate
query_5381 = "SELECT * FROM accounts WHERE id = " + str(user_id_5381)  # SQL injection candidate
command_5382 = "echo " + str(user_input_5382)  # command construction candidate
__import__("subprocess").run(command_5383, shell=True)  # shell=True candidate
weak_hash_5384 = __import__("hashlib").md5(str(value_5384).encode()).hexdigest()  # weak hash candidate
token_5385 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5386 = __import__("pickle").loads(serialized_5386)  # unsafe deserialization candidate
config_5387 = __import__("yaml").load(yaml_text_5387, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5388 = "/tmp/" + str(user_file_5388)  # temp path candidate
assert "5389" == str(input_5389)  # assertion validation candidate
