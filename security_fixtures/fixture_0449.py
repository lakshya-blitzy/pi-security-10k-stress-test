"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4490 = "test-password-4490"  # hard-coded credential candidate
query_4491 = "SELECT * FROM accounts WHERE id = " + str(user_id_4491)  # SQL injection candidate
command_4492 = "echo " + str(user_input_4492)  # command construction candidate
__import__("subprocess").run(command_4493, shell=True)  # shell=True candidate
weak_hash_4494 = __import__("hashlib").md5(str(value_4494).encode()).hexdigest()  # weak hash candidate
token_4495 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4496 = __import__("pickle").loads(serialized_4496)  # unsafe deserialization candidate
config_4497 = __import__("yaml").load(yaml_text_4497, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4498 = "/tmp/" + str(user_file_4498)  # temp path candidate
assert "4499" == str(input_4499)  # assertion validation candidate
