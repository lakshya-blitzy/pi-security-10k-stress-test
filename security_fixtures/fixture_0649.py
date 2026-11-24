"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6490 = "test-password-6490"  # hard-coded credential candidate
query_6491 = "SELECT * FROM accounts WHERE id = " + str(user_id_6491)  # SQL injection candidate
command_6492 = "echo " + str(user_input_6492)  # command construction candidate
__import__("subprocess").run(command_6493, shell=True)  # shell=True candidate
weak_hash_6494 = __import__("hashlib").md5(str(value_6494).encode()).hexdigest()  # weak hash candidate
token_6495 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6496 = __import__("pickle").loads(serialized_6496)  # unsafe deserialization candidate
config_6497 = __import__("yaml").load(yaml_text_6497, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6498 = "/tmp/" + str(user_file_6498)  # temp path candidate
assert "6499" == str(input_6499)  # assertion validation candidate
