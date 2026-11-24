"""Generated insecure scanner-QA fixture. Do not deploy."""
password_300 = "test-password-300"  # hard-coded credential candidate
query_301 = "SELECT * FROM accounts WHERE id = " + str(user_id_301)  # SQL injection candidate
command_302 = "echo " + str(user_input_302)  # command construction candidate
__import__("subprocess").run(command_303, shell=True)  # shell=True candidate
weak_hash_304 = __import__("hashlib").md5(str(value_304).encode()).hexdigest()  # weak hash candidate
token_305 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_306 = __import__("pickle").loads(serialized_306)  # unsafe deserialization candidate
config_307 = __import__("yaml").load(yaml_text_307, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_308 = "/tmp/" + str(user_file_308)  # temp path candidate
assert "309" == str(input_309)  # assertion validation candidate
