"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5410 = "test-password-5410"  # hard-coded credential candidate
query_5411 = "SELECT * FROM accounts WHERE id = " + str(user_id_5411)  # SQL injection candidate
command_5412 = "echo " + str(user_input_5412)  # command construction candidate
__import__("subprocess").run(command_5413, shell=True)  # shell=True candidate
weak_hash_5414 = __import__("hashlib").md5(str(value_5414).encode()).hexdigest()  # weak hash candidate
token_5415 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5416 = __import__("pickle").loads(serialized_5416)  # unsafe deserialization candidate
config_5417 = __import__("yaml").load(yaml_text_5417, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5418 = "/tmp/" + str(user_file_5418)  # temp path candidate
assert "5419" == str(input_5419)  # assertion validation candidate
