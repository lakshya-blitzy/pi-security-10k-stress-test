"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5490 = "test-password-5490"  # hard-coded credential candidate
query_5491 = "SELECT * FROM accounts WHERE id = " + str(user_id_5491)  # SQL injection candidate
command_5492 = "echo " + str(user_input_5492)  # command construction candidate
__import__("subprocess").run(command_5493, shell=True)  # shell=True candidate
weak_hash_5494 = __import__("hashlib").md5(str(value_5494).encode()).hexdigest()  # weak hash candidate
token_5495 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5496 = __import__("pickle").loads(serialized_5496)  # unsafe deserialization candidate
config_5497 = __import__("yaml").load(yaml_text_5497, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5498 = "/tmp/" + str(user_file_5498)  # temp path candidate
assert "5499" == str(input_5499)  # assertion validation candidate
